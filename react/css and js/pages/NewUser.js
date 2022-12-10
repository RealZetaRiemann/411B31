import './enterZipcode.css';

const NewUser = () => {
	return (


<div>


<h1>Weather Spoons</h1>
<p>Welcome to Weather Spoons! Please enter your zipcode so we can recommend some tasty recipes 
  And don't worry! We'll remember your zipcode for next time, so you only have to enter it once 
  unless you need to change it.</p>

  <div id="main">
      {% if failure == True %}
          <p>Please enter a valid zipcode to continue.</p>
      {% endif %}
      <div id="start">
          <form action = "/home" method = "POST" id="enteruser">
              <p style = "text-align: center;"><input type="text" name="zipcode" placeholder="Your Zipcode" required/></p>
              <p style = "text-align: center;"><input type = "submit" value = "submit"/></p>
          </form>
      </div>
  </div>

  </div>

)


}

export default NewUser