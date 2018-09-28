import React from 'react';

import Button from './button';
export default ({firstname, lastname, email, following, skills, preferences, blurred, link, buttonText }) =>
    <div className='card'>
        <h2 className={blurred ? 'blurred-text' : ''}>{firstname + ' ' + lastname }</h2>
        <p><span className='label'>Following:</span> {following}</p>
        <p><span className='label'>Skills:</span> {skills}</p>
        <p><span className='label'>Preferences:</span> {preferences}</p>
        <Button text={buttonText} link={link ? link : {href: '/', state: {}}}/>
    </div>