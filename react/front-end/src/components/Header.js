import Button from './Button'

const Header = ({title}) => {
  const onClick = () => {
	console.log('Clicked')
  }
  
  return (
	<header className='header'>
		<h1>{title}</h1>
		<Button onClick={onClick} text='test' />
	</header>
  )
}

export default Header