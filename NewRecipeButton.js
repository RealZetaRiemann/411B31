import React, { useState } from "react";
import styled from "styled-components";

const theme = {
  blue: {
    default: "#3f51b5",
    hover: "#283593"
  },
  pink: {
    default: "#e91e63",
    hover: "#ad1457"
  }
};

const Button = styled.button`
  background-color: ${(props) => theme[props.theme].default};
  color: white;
  padding: 5px 15px;
  border-radius: 5px;
  outline: 0;
  text-transform: uppercase;
  margin: 10px 0px;
  cursor: pointer;
  box-shadow: 0px 2px 2px lightgray;
  transition: ease background-color 250ms;
  &:hover {
    background-color: ${(props) => theme[props.theme].hover};
  }
  &:disabled {
    cursor: default;
    opacity: 0.7;
  }
`;

Button.defaultProps = {
  theme: "blue"
};

function goToNewRecipe(){
useEffect(() => {
  // Using fetch to fetch the api from 
  // flask server it will be redirected to proxy
  fetch("/home/").then((res) =>
      res.json().then((data) => {
          // Setting a data from api
          setdata({
              forecast: data.forecast,
              image: data.image,
              sourceUrl: data.sourceUrl,
              city: data.city,
              zipcode: data.zipcode
          });
      })
  );
}, []);
}

export default function App() {
  return (
    <>
     
      <a href="https://react.school" target="_blank">
        <Button>onClick={() => goToNewRecipe}New Recipe</Button>
      </a>
    </>
  );
}
const domContainer = document.querySelector('#like_button_container');
const root = ReactDOM.createRoot(domContainer);
root.render(e(LikeButton));
