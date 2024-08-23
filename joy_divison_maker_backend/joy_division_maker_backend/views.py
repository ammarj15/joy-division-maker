from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from PIL import Image, ImageDraw
import io
import base64
import numpy as np
from datetime import datetime

class GenerateImageView(APIView):
    #in memory storage for last 10 generations
    image_history = []

    def get(self, request):
       
        high_res_scale = 10  # Reduce the scale factor for less change
        size = 340
        high_res_size = size * high_res_scale
        
        image = Image.new('RGB', (high_res_size, high_res_size), (0, 0, 0))
        draw = ImageDraw.Draw(image)
        line_width = 3 * high_res_scale  # Scale the line width
        step = 9 * high_res_scale  # Scale the step size
        
        # Make Joy Division Poster using PIL lib
        lines = []
        for i in range(500 , high_res_size - step, step):
            line = []
            for j in range(step, high_res_size - step, step):
                distance_to_center = abs(j - high_res_size / 2)
                variance = max(high_res_size / 2 - 700 - distance_to_center, 0)
                random_offset = np.random.uniform(-variance / 2, 0)
                point = (j, i + random_offset)
                line.append(point)
            lines.append(line)

        # Draw the lines with curves
        for line in lines:
            if len(line) > 1:
                for k in range(len(line) - 1):
                    start_point = line[k]
                    end_point = line[k + 1]

                    control_point = ((start_point[0] + end_point[0]) / 2, (start_point[1] + end_point[1]) / 2)
                    
                    draw.line([start_point, control_point, end_point], fill=(255, 255, 255), width=int(line_width))

        # Downscale the image with bilinear resampling
        image = image.resize((size, size), resample=Image.Resampling.BILINEAR)
        
        buffer = io.BytesIO()
        image.save(buffer, format='PNG')
        image_data = base64.b64encode(buffer.getvalue()).decode('utf-8')

        #Store image in memory
        self.save_image(image_data)

        # Return base64 img data as JSON
        return Response({'image': f'data:image/png;base64,{image_data}'})
    
    def save_image(self, image_data):
        timestamp = datetime.now().isoformat()
        self.image_history.append({'image': image_data, 'timestamp': timestamp})

        #Ensure only last 10
        if len(self.image_history) > 10:
            self.image_history.pop(0)

class ImageHistoryView(APIView):
    def get(self, request):
        return Response(GenerateImageView.image_history)