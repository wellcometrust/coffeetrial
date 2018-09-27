import Button from './button';
export default ({name, following, skills, preferences}) =>
    <div className='card'>
        <h2>{name}</h2>
        <p><span className='label'>Following:</span> {following}</p>
        <p><span className='label'>Skills:</span> {skills}</p>
        <p><span className='label'>Preferences:</span> {preferences}</p>
        <Button text='select' link='/'/>
    </div>