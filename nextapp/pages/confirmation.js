import "../css/styles.scss";
import Button from '../components/button';
import Colleague from '../components/colleague';
export default () =>
    <div>
        <h1>Looking forward to meet Christine?</h1>
        <p>We have sent an email to both of you so that you can arrange your Coffee trial.
            Please make sure you manage to meet up by 30. November 2018 at the latest.
            You will meet:
        </p>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Button text={'Invite Christine'}/>
    </div>