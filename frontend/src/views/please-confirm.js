import React from 'react';
import Colleague from '../components/colleague';
import Button from '../components/button';
export default class PleaseConfirm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            matches: [],
            userId: '1',
            match: props.location.state.match,
            matchType: props.location.state.matchType ? props.location.state.matchType : null
        };
    }

    componentDidMount() {
        if (this.state.matchType === 'random') {
            console.log('haiii');
        } else {
            fetch('/match', {
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    user_1_id: this.state.userId,
                    user_2_id: this.state.match.id,
                })
            })
                .then(res => res.json())
                .then(
                    (result) => {
                        console.log(result);
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
                    <img className="coffee-gif" src="https://media1.tenor.com/images/af7654602fd50d8f32b277db914cb14d/tenor.gif?itemid=8616709"/>
                    <h1> We have found you a Coffeetrial colleague</h1>
                    <Colleague
                        firstname={this.state.match.firstname}
                        lastname={this.state.match.lastname}
                        preferences='cappicuno'
                        skills='SQL, Databases'
                        following='Trustnet fanclub'
                        buttonText='Ok, thanks'
                        link={{
                            href: '/confirmation',
                            state: {match: this.state.match}}}
                    />
                    <h2>Can't accept?</h2>
                    <p>If you happen to know Christine already, you can start again.</p>
                    <Button text={'Start again'} link={{href: '/match-maker', state: {}}}/>
                </div>
            );
        }
    }
}