import React from 'react';
import Button from '../components/button';
import Colleague from '../components/colleague';

export default () =>
    <div className="page">
        <img className="coffee-gif" src="https://media1.tenor.com/images/af7654602fd50d8f32b277db914cb14d/tenor.gif?itemid=8616709"/>
        <h1> We have found you a Coffeetrial colleague</h1>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <h2>Can't accept?</h2>
        <p>If you happen to know Christine already, you can start again.</p>
        <Button text={'Start again'}/>
    </div>