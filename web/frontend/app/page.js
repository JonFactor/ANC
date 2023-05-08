import Image from 'next/image'
import styles from './page.module.css'
import Link from 'next/link'
import Hero from './components/landing/Hero'
import Quickstart from './components/landing/Quickstart'
import BackroundAbsolutes from './components/landing/BackroundAbsolutes'

export default function Home() {
  
  
  return (
    <main className='  '>
      <BackroundAbsolutes />
      <Hero />
      <Quickstart />
      <div id='filler' className=' bg-black w-[1px] h-[400px]'/>
    </main>
  )
}
