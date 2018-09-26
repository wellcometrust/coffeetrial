import "../css/styles.scss";
import Button from '../components/button';
export default () =>
    <div>
        <h1> Hi, find your Coffeetrial colleague  </h1>
        <p>The next round of Random Coffee Trials will take place from
            1. - 30. November 2018. 541 colleagues have signed up to take part.</p>
        <div>
            <h2>Take your (random) pick</h2>
            <p>
                You will be matched randomly, but, if you like –and if you are quick– you can have a bit of a say who you will be meeting.
            </p>
            <p>
                If you have not been matched already, you can pick a colleague for the next round from a random shortlist of 3 candidates.
            </p>
            <Button text='Take your pick'/>
        </div>
        <h2>Don't want to pick?</h2>
        <p>
            No problem. If you don't do anything, you will be automatically matched with a colleague. As ususal, you will receive an email as soon as you have been matched.
        </p>
        <h2> Can't make it this time?</h2>
        <p>
            No problem. Just skip this round.
        </p>
    </div>