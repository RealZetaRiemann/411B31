import './recipeFound.css';


const Favorites = () => {
  return (

	<div>
	


        <ul>
            <li><a href="/profile">Profile</a></li>
            <li><a className="active" href="/favorites">Favorites</a></li>
            <li><a href="/home">New Recipes</a></li>
            <li><a href="/newuser">Zipcode</a></li>
            <li style="float:right"><a href="/index">Sign Off</a></li>
        </ul>



        <div className="two-boxes">


        <div className="recipe-box">
            <h1> Favorite </h1>
        </div>

        </div>

        <div className="results-box">
        <a href="" target="_blank" style="font-size: 25px; color:black;"> {{title}} </a>
        <br/><img src="{{image}}" alt="recipe preview"/>
        </div>

	
	</div>





  )
}

export default Favorites