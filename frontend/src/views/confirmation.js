import "../css/styles.scss";
import Button from '../../frontend/src/components/button';
import Colleague from '../../frontend/src/components/colleague';
import Header from '../../frontend/src/components/header';

export default () =>
    <div className="page">
        <Header/>
        <img src ='coffee-gif' src="https://www.youreduaction.it/wp-content/uploads/2015/06/ci-offri-un-caff%C3%A8.gif"/>
        <h1>Looking forward to meet Christine?</h1>
        <p>We have sent an email to both of you so that you can arrange your Coffee trial.
            Please make sure you manage to meet up by 30. November 2018 at the latest.
            You will meet:
        </p>
        <Colleague name='fred' preferences='cappicuno' skills='SQL, Databases' following='Trustnet fanclub'/>
        <Button text={'Invite Christine'}/>
    </div>