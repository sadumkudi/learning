class App extends Component {
    constructor(){
        super()
        this.state = {
            loggedIn: true
        }  
        this.handleSubmit = this.handleSubmit.bind(this)     
    }
    handleSubmit(){
        console.log("clicked to login")
        this.setState(prevState => {
            return {
                loggedIn: !prevState.loggedIn 
            }
        })
        console.log(this.state.loggedIn)
    }
    
    render(){
       return (
            <div>
                <h1>{this.state.loggedIn? 'Logged in': 'Logged out'}</h1>           
                <button type="submit" onClick={this.handleSubmit}>{this.state.loggedIn? 'Log out': 'Log in'} </button>
             </div>   
        )    
    }
}

export default App
