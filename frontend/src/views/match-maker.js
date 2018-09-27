import "../css/styles.scss";
import Colleague from '../../frontend/src/components/colleague';
import Button from '../../frontend/src/components/button';
import Header from '../../frontend/src/components/header';

export default () =>
    <div className="page">
        <Header/>
        <h1>What about coffee with one of these colleagues?</h1>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Colleague name='George' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Colleague name='Ron' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <h2>Can't decide?</h2>
        <p>We will find you a complete random match.</p>
    <Button text='Get me anyone'/>
    </div>