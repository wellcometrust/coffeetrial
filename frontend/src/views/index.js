import React from 'react';
import LinkButton from '../components/linkbutton';
import Colleague from '../components/colleague';
export default () =>
<div className="page">
    <h1> Welcome </h1>
    <p> Random Coffeetrials are a fun way to get to know new colleagues. </p>
    <h2>I'm happy to take part</h2>
    <LinkButton text={'Yes'} link={{href: '/take-your-pick'}}/>
    <LinkButton text={'No'} link={{href: '/'}}/>
    <h2>Next round</h2>
    <p>The next round of Random Coffee Trials will take place from 1.-30. November 2018.</p>
    <a href="/">Find a random match</a> or
    <a href="/">View paired colleague</a>
    <a href="/">Skip round</a>
    <h2>Profile</h2>
    <Colleague
        firstname='Ben'
        lastname='Smith'
        following='Wellbeing, Volunteering, Wellies'
        skills='SQL, Data Analysis, excel'
        buttonText='Update profile on trustnet'
        link={{href: '/'}}
    />
</div>
