import React from 'react';
import {Link} from 'react-router-dom';

export default ({text, link}) =>
        <Link to={{
            pathname: link.href,
            state: link.state
        }}
        className="button-like">
        {text}
        </Link>
