import React from 'react';
import Colleague from '../components/colleague';
export default class Confirmation extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userId: '1',
            match: props.location.state.match,
        };
    }

    render() {
        const {match} = this.state;
        return (
            <div className="page">
                <h1>Looking forward to meet {match.firstname} {match.lastname}?</h1>
                <p>We have sent an email to both of you so that you can arrange your Coffee trial.
                    Please make sure you manage to meet up by 30. November 2018 at the latest.
                    You will meet:
                </p>
                <Colleague
                    firstname={match.firstname}
                    lastname={match.lastname}
                    preferences='Instant coffee'
                    skills='SQL, Databases'
                    following='Trustnet fanclub'
                    buttonText={'Invite ' + match.firstname + ' ' + match.lastname}
                    link={{
                        href: '/',
                        state: {match: match}
                    }}
                />
            </div>
        );

    }

}