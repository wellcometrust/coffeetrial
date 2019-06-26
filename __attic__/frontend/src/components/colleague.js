import React from 'react';

import LinkButton from './linkbutton';
export default ({firstname, lastname, email, following, skills, preferences, blurred, link, buttonText }) =>
    <div className='card'>
        <h2 className={blurred ? 'blurred-text' : ''}>{firstname + ' ' + lastname }</h2>
        <p><span className='label'>Following:</span> {following}</p>
        <p><span className='label'>Skills:</span> {skills}</p>
        <p><span className='label'>Preferences:</span> {preferences}</p>
        <LinkButton text={buttonText} link={link ? link : {href: '/', state: {}}}/>
    </div>
