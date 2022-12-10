import { Link, useMatch, useResolvedPath } from 'react-router-dom';

const Navbar = () => {
  const path = window.location.pathname
  return (
	<nav>
		<Link to="/" className="site-title">weatherspoons</Link>
		<ul>
			<CustomLink to="/home">Home</CustomLink>
			<CustomLink to="/profile">Profile</CustomLink>
		</ul>
	</nav>
  )
}

function CustomLink({ to,children, ...props }){
	const resolvedPath = useResolvedPath(to)
	const isActive = useMatch({ path: resolvedPath.pathname, end: true})
	return (
		<li className={isActive ? "active" : ""}>
			<Link to={to} {...props}>
				{children}
			</Link>
		</li>
	)
}

export default Navbar