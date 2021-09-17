// import logo from './logo.svg';
import './App.css';
import React from 'react';


class App extends React.Component {					
	
	render() {
    return (
      <div>
        <h1><font bg = "black" color="gold">Welcome to Bookinfo(site under construction, stay tuned...)</font></h1>
        <button type="button" underlayColor="gold" onClick={this.changeValue}>Login</button>
        <button type="button" underlayColor="gold" onClick={this.changeValue}>Sign up</button>
      </div>
    );
  }
}

export default App;
