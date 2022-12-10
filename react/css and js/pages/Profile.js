import './profile.css';



const Profile = () => {
  return (

	<div>
	
	  <ul>
		<li><a className="active" href="/profile">Profile</a></li>
		<li><a href="/favorites">Favorites</a></li>
		<li><a href="/home">New Recipes</a></li>
		<li><a href="/newuser">Zipcode</a></li>
		<li style="float:right"><a href="/index">Sign Off</a></li>
	</ul>
	
	

	
	
	
	  <div className="container">
		  <img className="image" src="{{ avatar }}" />
	  </div>
	
	
	  <div className="profile-box">
		  <h1> <strong><u>Profile</u> </strong></h1>
		  <p>Username: {{username | safe}}</p>
		  <p>Real Name: {{realname | safe}}</p>
		  <p>Zipcode: {{zipcode | safe}}</p>
	  </div>
	
	
	</div>





  )
}

export default Profile