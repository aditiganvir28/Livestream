// VideoStream.js
import React, { useState, useEffect } from 'react';
import io from 'socket.io-client';

const VideoStream = () => {
  const [video, setVideo] = useState(null);

  const video_url = 'http://localhost:5000/video_feed'

  // useEffect(() => {
  //   const socket = io('ws://localhost:8080');

  //   socket.on('frame', (frame) => {
  //     setVideo(frame);
  //   });

  //   return () => {
  //     socket.disconnect();
  //   };
  // }, []);

  // const videoRef = useRef(null);

  // useEffect(() => {
  //   async function fetchVideo() {
  //     try {
  //       const response = await axios.get('http://localhost:5000/video', {
  //         responseType: 'blob', // Ensure binary data is received correctly
  //       });

  //       // Create a URL for the blob data
  //       const videoBlob = new Blob([response.data], { type: 'video/mp4' });
  //       const videoUrl = URL.createObjectURL(videoBlob);

  //       // Set the video source
  //       videoRef.current.src = videoUrl;
  //     } catch (error) {
  //       console.error('Error fetching video:', error);
  //     }
  //   }
  // }
  // )

  // if (!video) {
  //   return <div>Loading...</div>;
  // }

  return (
    <>
    {/* <video src={video} controls /> */}
    <img src={video_url}></img>
    {/* <video ref={videoRef} controls width="640" height="480" /> */}
    </>
  );
};

export default VideoStream;



