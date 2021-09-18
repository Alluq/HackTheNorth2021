import "./App.css"
import { useState } from "react";
import SubmitForm from "./components/SubmitForm";
import { BrowserRouter as Router, Route} from 'react-router-dom'
import { Redirect } from "react-router";
import Dashboard from "./components/Dashboard";
import Login from "./components/Login"

function App() {

  const [fileUploaded, setFileUploaded] = useState(0);

  const [fileName, setFileName] = useState("");

  const checkIfLoggedIn = () => {
    let loggedIn = false

    //Add login Logic

    return loggedIn
  }


  return (
    <Router>
      <div className="App">
        <Route path="/"  exact render={(props) => checkIfLoggedIn() == false ? 
        <Dashboard/> : <Redirect to={{pathname: "/login", state : {from: props.location}}}/>} />
        <Route path="/login" component={Login}/>
      </div>
    </Router>
  );
}

export default App;
