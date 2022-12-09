import Navbar from './components/Navbar';
import Home from './pages/Home';
import Profile from './pages/Profile';
import { useState,useEffect } from 'react';
import jwtDecode from 'jwt-decode';
import { Route, Routes } from 'react-router-dom';

function App() {
  //on callback from google oauth
  function handleCallbackResponse(response){
    console.log("Encoded JWT ID token: "+response.credential);
    //parse jwt
    var userObject = jwtDecode(response.credential);
    //POST request containing userdata
    const requestOptions = {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ picture: userObject.picture, userID: userObject.sub, email: userObject.email, given_name: userObject.given_name })
    };
    fetch('http://localhost:5000/login', requestOptions)
    console.log(userObject);
    console.log(requestOptions);
  }

  useEffect(() => {
    /*global google*/
    google.accounts.id.initialize({
      client_id: "769125758041-46jcr3mu4id8f9i4k3d84sd5qb7nav10.apps.googleusercontent.com",
      callback: handleCallbackResponse
    });

    google.accounts.id.renderButton(
      document.getElementById("signInDiv"),
      { theme: "outline", size: "large"}
    )
  }, []);

  return ( 
    <>
      <Navbar />
      <div className="container">
        <Routes>
          <Route path="/" element={<div id="signInDiv"></div>} />
          <Route path="/profile" element={<Profile />} />
          <Route path="/home" element={<Home />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
