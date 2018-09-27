import React from 'react';
import Button from '../components/button';
import Colleague from '../components/colleague';
export default () =>
<div className="page">
    <h1> Welcome </h1>
    <p> Random Coffeetrials are a fun way to get to know new colleagues. </p>
    <h2>I'm happy to take part</h2>
    <Button text={'Yes'} link={{href: '/take-your-pick', state: {}}}/>
    <Button text={'No'} link='/'/>
    <h2>Next round</h2>
    <p>The next round of Random Coffee Trials will take place from 1.-30. November 2018.</p>
    <a>Find a random match</a> or
    <a>View paired colleague</a>
    <a>Skip round</a>
    <h2>Profile</h2>
    <Colleague name='Ben Smith' following='Wellbeing, Volunteering, Wellies' skills='SQL, Data Analysis, excel'/>
</div>
