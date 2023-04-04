import './globals.css'

export const metadata = {
  title: 'ANC',
  description: 'what a good site.',
}

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
