import Image from 'next/image'
import styles from './page.module.css'
import Link from 'next/link'
import Hero from './components/Hero'


export default function Home() {
  return (
    <main className='  '>
      <Hero />
      <div id='filler' className=' bg-black w-[1px] h-[400px]'/>
    </main>
  )
}
