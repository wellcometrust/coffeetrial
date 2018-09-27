import Link from 'next/link'
export default ({text, link}) =>
    <button>
        <Link href={link}>
        {text}
        </Link>
    </button>