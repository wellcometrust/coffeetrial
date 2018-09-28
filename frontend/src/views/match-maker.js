import React from 'react';
import Colleague from '../components/colleague';
import Button from '../components/button';
export default class MatchMaker extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            matches: [],
            userId: '1',
        };
    }

    componentDidMount() {
        fetch("/match/1")
            .then(res => res.json())
            .then(
                (result) => {
                    setTimeout(()=>{
                        this.setState({
                            isLoaded: true,
                            matches: result
                        });
                    }, 2000);

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
            return <img src='https://payload484.cargocollective.com/1/15/505014/11995996/ErrorPage_Connection_Dino_4.gif' className="loading-gif"/>
        } else if (!isLoaded) {
            return <div className="page">
                    <img src='https://ph-files.imgix.net/5325ada6-b985-47d0-b37f-6dc2520e4076?auto=format&auto=compress&codec=mozjpeg&cs=strip' class="loading-gif"/>
                </div>
            } else {
            return (
                <div className="page">
                    <h1>What about coffee with one of these colleagues?</h1>
                    {
                        matches.map((match)=>
                            <Colleague
                                firstname={match.firstname}
                                lastname={match.lastname}
                                email={match.email}
                                preferences='Instant Coffee'
                                skills='SQL, Databases'
                                following='Trustnet fanclub'
                                blurred={true}
                                link={{
                                    href: '/please-confirm',
                                    state: {user_id: '1', match: match}
                                }}
                                buttonText='select'
                            />)
                    }
                    <h2>Can't decide?</h2>
                    <p>We will find you a complete random match.</p>
                    <Button text='Get me anyone' link={{href: '/please-confirm', state: {matchType: 'random'} }}/>
                </div>
            );
        }
    }
}
