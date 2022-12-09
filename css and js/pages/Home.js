import './recipeFound.css';

const Home = () => {
	return (
	

	<div>


	<ul>
	  <li><a href="/profile">Profile</a></li>
	  <li><a href="/favorites">Favorites</a></li>
	  <li><a className="active" href="/home">New Recipes</a></li>
	  <li><a href="/newuser">Zipcode</a></li>
	  <li style="float:right"><a href="/index">Sign Off</a></li>
  </ul>
  
  
  
  <div className="two-boxes">
  
	<div className="recipe-box">
	  <h1> Recipe Found! </h1>
	</div>
  
	<div className="weather-box">
	  <p>    The weather in {{city}} {{zipcode}} is currently {{forecast}} <br/>
		based on the weather, we recommend this recipe: </p>
	</div>
  
  </div>
  
  <div className="results-box">
	<a href={{sourceUrl}} target="_blank" style="font-size: 25px; color:black;">{{title}}</a>
	<br/><img src="{{image}}" alt="recipe preview"/>
	<button href=""className="Fav-button"> &#9733; Favorite </button>
	
  </div>


  </div>



	)


}

export default Home