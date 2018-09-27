import React from 'react';
import {Link} from 'react-router-dom';

export default ({text, link}) =>
    <button>
        <Link to={{
            pathname: link.href,
            state: link.state
        }}>
        {text}
        </Link>
    </button>