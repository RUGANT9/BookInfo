import React from 'react';
import './App.css';
import Navbar from './components/Navbar';
import { BrowserRouter as Router, Switch, Route } from 'react-router-dom';
import Home from './pages';
import About from './pages/about';
import SignUp from './pages/signup';
  
function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route path='/' exact component={Home} />
        <Route path='/about' component={About} />
        <Route path='/sign-up' component={SignUp} />
      </Switch>
    </Router>
  );
}
  
export default App;
// import logo from './logo.svg';
// import './App.css';
// import React from 'react';


// class App extends React.Component {					
	
// 	render() {
//     return (
//       <div>
//         <h1><font bg = "black" color="gold">Welcome to Bookinfo(site under construction, stay tuned...)</font></h1>
//         <button type="button" underlayColor="gold" onClick={this.changeValue}>Login</button>
//         <button type="button" underlayColor="gold" onClick={this.changeValue}>Sign up</button>
//       </div>
//     );
//   }
// }

// export default App;
