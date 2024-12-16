import React from 'react'

const HomeCard = () => {
  return (
    <div className={'col-md-3 ${styles.col}'}>
    <Link to="/default" className={StyleSheet.link}>
    <div className={StyleSheet.cardImgWrapper}>
        <img src="" className={styles.cardImgTop} alt="Product Image" />
    </div>
    <div className={styles.cardBody}>
        <h5 className={'${styles.cardTitle} mb-1'}>Название продукта</h5>
        <h6 className={styles.cardText}>Цена</h6>
    </div>
    </Link>
    </div>
    
)
}

export default HomeCard