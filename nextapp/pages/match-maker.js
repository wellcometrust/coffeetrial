import "../css/styles.scss";
import Colleague from '../components/colleague';
import Button from '../components/button';
export default () =>
    <div>
        <h1>What about coffee with one of these colleagues?</h1>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Colleague name='George' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Colleague name='Ron' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <h2>Can't decide?</h2>
        <p>We will find you a complete random match.</p>
    <Button text='Get me anyone'/>
    </div>