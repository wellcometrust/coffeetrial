import Button from '../components/button';
import Colleague from '../components/colleague';
import Header from '../components/header';
import React from 'react';


export default () =>
    <div className="page">
        <img src ='coffee-gif' src="https://www.youreduaction.it/wp-content/uploads/2015/06/ci-offri-un-caff%C3%A8.gif"/>
        <h1>Looking forward to meet Christine?</h1>
        <p>We have sent an email to both of you so that you can arrange your Coffee trial.
            Please make sure you manage to meet up by 30. November 2018 at the latest.
            You will meet:
        </p>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Button text={'Invite Christine'} link='/'/>
    </div>