import "../css/styles.scss";
import Button from '../components/button';
import Colleague from '../components/colleague';
export default () =>
    <div>
        <h1> We have found you a Coffeetrial colleague</h1>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <h2>Can't accept?</h2>
        <p>If you happen to know Christine already, you can start again.</p>
        <Button text={'Start again'}/>
    </div>