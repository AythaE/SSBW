import React, { Component } from "react";
import "./App.css";
import "bootstrap/dist/css/bootstrap.css";
import { Navbar, NavItem, Nav, Grid, Row, Col } from "react-bootstrap";
import "bootswatch/cerulean/bootstrap.css";
var S = require('string');

const LUGARES = [
  { name: "Granada"},
  { name: "Salamanca" },
  { name: "Burgos" },
  { name: "Madrid" }
];

class WeatherDisplay extends Component {
    constructor() {
    super();
    this.state = {
      weatherData: null
    };
  }
  componentDidMount() {
    const city = this.props.city;
    console.log(city)
    const URL = "http://api.openweathermap.org/data/2.5/weather?q=" +
      city + ",es"+
      "&appid=552ae2302821d57861d94e982b66822a&units=metric&lang=es";
    fetch(URL).then(res => res.json()).then(json => {
      this.setState({ weatherData: json });
    });
  }
  render() {
      const weatherData = this.state.weatherData;
      if (!weatherData) return <div>Cargando</div>;
      const weather = weatherData.weather[0];
      const iconUrl = "http://openweathermap.org/img/w/" + weather.icon + ".png";
      const description = S(weather.description).capitalize().s
      return (
        <div>
          <h1>
            {description} en {weatherData.name}
            <img src={iconUrl} alt={weatherData.description} />
          </h1>
          <p>Actual: {weatherData.main.temp}°</p>
          <p>Máxima: {weatherData.main.temp_max}°</p>
          <p>Mínima: {weatherData.main.temp_min}°</p>
          <p>Velocidad del viento: {weatherData.wind.speed} m/s</p>
        </div>
    );
  }
}

class App extends Component {
  constructor() {
    super();
    this.state = {
      activePlace: 0
    };
  }

  render() {
    const activePlace = this.state.activePlace;
    return (
      <div className="App">
      <div>
        <Navbar>
          <Navbar.Header>
            <Navbar.Brand>
              Tiempo ReactJS
            </Navbar.Brand>
          </Navbar.Header>
        </Navbar>
        <Grid>
          <Row>
            <Col md={4} sm={4}>
              <h3>Elija una ciudad</h3>
              <Nav
                bsStyle="pills"
                stacked
                activeKey={activePlace}
                onSelect={index => {
                  this.setState({ activePlace: index });
                }}
              >
                {LUGARES.map((place, index) => (
                  <NavItem key={index} eventKey={index}>{place.name}</NavItem>
                ))}
              </Nav>
            </Col>
            <Col md={8} sm={8}>
              <WeatherDisplay key={activePlace} city={LUGARES[activePlace].name} />
            </Col>
          </Row>
        </Grid>
        </div>

      </div>
    );
  }
}

export default App;
