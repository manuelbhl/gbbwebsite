
const modal = document.querySelector("#modal");
       const openModal = document.querySelector(".open-button");
       const closeModal = document.querySelector(".close-button");
       const closeModal2 = document.querySelector(".close-button2");

       openModal.addEventListener("click", () => {
         modal.showModal();
       });
       
       closeModal.addEventListener("click", () => {
         modal.close();
       });
       closeModal2.addEventListener("click", () => {
              modal.close();
            });

        const modalvid = document.querySelector("#modalvid");
            const openModalvid = document.querySelector(".open-buttonvid");
            const closeModalvid = document.querySelector(".close-buttonvid");
            const closeModalvid2 = document.querySelector(".close-buttonvid2");

            openModalvid.addEventListener("click", () => {
              modalvid.showModal();
            });
            
            closeModalvid.addEventListener("click", () => {
              modalvid.close();
            });
            closeModalvid2.addEventListener("click", () => {
              modalvid2.close();
            });
