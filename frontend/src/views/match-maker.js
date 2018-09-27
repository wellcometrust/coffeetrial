import React from 'react';
import Colleague from '../components/colleague';
import Button from '../components/button';
export default class MatchMaker extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            matches: []
        };
    }

    componentDidMount() {
        fetch("/match/1")
            .then(res => res.json())
            .then(
                (result) => {
                    this.setState({
                        isLoaded: true,
                        matches: result
                    });
                },
                // Note: it's important to handle errors here
                // instead of a catch() block so that we don't swallow
                // exceptions from actual bugs in components.
                (error) => {
                    this.setState({
                        isLoaded: true,
                        error
                    });
                }
            )
    }

    render() {
        const { error, isLoaded, matches } = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            return (
                <div className="page">
                    <h1>What about coffee with one of these colleagues?</h1>
                    {
                        matches.map((match)=>
                            <Colleague
                                firstname={match.firstname}
                                id={match.id}
                                lastname={match.lastname}
                                email={match.email}
                                preferences='Instant Coffee'
                                skills='SQL, Databases'
                                following='Trustnet fanclub'
                                blurred={true}
                                link={{href: ''}}
                            />)
                    }
                    <h2>Can't decide?</h2>
                    <p>We will find you a complete random match.</p>
                    <Button text='Get me anyone' link='/'/>
                </div>
            );
        }
    }
}
