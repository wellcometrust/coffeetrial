import React from 'react';
import {Link} from 'react-router-dom';

export default ({text, link}) =>
    <button>
        <Link to={link}>
        {text}
        </Link>
    </button>