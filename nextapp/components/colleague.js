import Button from './button';
export default ({name, following, skills, preferences}) =>
    <div>
        <p>{name}</p>
        <p>Following: {following}</p>
        <p>Skills: {skills}</p>
        <p>Preferences: {preferences}</p>
        <Button text='select'/>
    </div>