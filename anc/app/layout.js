import './globals.css'
import Navbar from './components/Navbar'

export default function RootLayout({ children }) {

  return (
    <html lang="en">
      <head />
      <body className=''>
        <Navbar/>
        {children}
      </body>
    </html>
  )
}
