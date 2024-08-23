import React, { useEffect, useRef, useState } from 'react';
import '../styles/Canvas.scss';
import Button from './Button';
import History from './History';

function Canvas() {
    const [imageData, setImageData] = useState(null);
    const canvasRef = useRef(null);
    const [history, setHistory] = useState([]);

    const generateImage = async () => {
        const response = await fetch('http://localhost:8000/api/generate-image/');
        const data = await response.json();
        setImageData(data.image);
    };

    const displayHistory = async () => {
        const response = await fetch('http://localhost:8000/api/history/');
        const data = await response.json();
        setHistory(data);
    };

    useEffect(() => {
        if (imageData) {
            const canvas = canvasRef.current;
            const ctx = canvas.getContext('2d');

            const img = new Image();
            img.onload = () => {
                // Draw image on canvas
                ctx.clearRect(0, 0, canvas.width, canvas.height);
                ctx.drawImage(img, 0, 0, canvas.width, canvas.height);
            };
            img.src = imageData;
        }
    }, [imageData]);

    return (
        <div>
            <div className='relative-container'>
                <div className='buttons'>
                    <Button onClick={generateImage}>Generate Image</Button>
                    <Button onClick={displayHistory}>Show last 10 generations</Button>
                </div>
                <canvas
                    ref={canvasRef}
                    width="320"
                    height="320"
                    style={{ border: '1px solid black' }}
                ></canvas>
            </div>
            <History history={history} />
        </div>
    );
}

export default Canvas;
