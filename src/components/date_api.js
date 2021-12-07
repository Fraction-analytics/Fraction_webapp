import React, { Component } from 'react'
import axios from 'axios'
import { Player } from 'video-react';
// import '../App.css'

class PostForm extends Component {
    constructor(props) {
        super(props)

        this.state = {
            key: '10-10-21',
            // Where data will be saved.
            links: [],
        }
        console.log(this.state)
    }

    changeHandler = e => {
        this.setState({ [e.target.name]: e.target.value })
    }

    submitHandler = e => {
        e.preventDefault()
        
        axios
        .get(`http://127.0.0.1:8000/hvals_hash?key=${this.state.key}`)
        .then(response => {
                        // Updating the state to trigger a re-render       
            this.setState({links: response.data});
            console.log(response)
            // console.log(this.state.links)
        })
        .catch(error => {
            console.log(error)
        })
    }

    render() {
        const { key } = this.state
        
        return (
            <center><div>
                <form onSubmit={this.submitHandler}>
                    <div>
                        <h2> DATE PICKER</h2><br></br>
                        <input
                            type="text"
                            name="key"
                            value={key}
                            onChange={this.changeHandler}
                        />
                        
                    </div>
                    <br></br>
                    <button type="submit">Submit</button>
                </form>
                {this.state.links.map((link, i) => { 
                    return (
                    
                    <div key={i}>
                
                        <Player>
                            <source src={link} />
                        </Player>
                </div> 
                )})}
        
            </div></center>
        )
    }
}
export default PostForm