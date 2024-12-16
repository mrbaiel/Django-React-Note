import React from 'react'

const Header = () => {
  return (
    <header>
        <div className='py-5' style={{backgroundColor: '#6050DC'}}>
            <div className='text-center text-white'>
                <h1 className='display-4 fw-bold'>Добро пожаловать)</h1>
                <p className='lead fw-normal text-white-75 mb-4'>Последние тренды</p>
                <a href="#shop" className='btn btn-light btn-lg rounded-pill px-4 py-2'></a>
            </div>
            
        </div>
    </header>

  )
}

export default Header