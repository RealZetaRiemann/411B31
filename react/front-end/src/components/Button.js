const Button = ({color,onClick,text}) => {
  return (
	<button 
	  onClick={onClick}
	  style={{backgroundColor: color}}
	  className='butt'
	>
	  {text}
	</button>
  )
}


export default Button