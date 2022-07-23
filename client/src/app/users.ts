const getSammyBear = () => {
    let id = "4298cec0-1862-4638-bd9d-7b70b387753b";
    let userId = "b08103e8-942e-475d-9fe5-45795bfe717f";
    let email = "sammybear@local.com";
    let is_technician = true;
    let is_client = false;
    let name = "Sammy Bear";

    return {
        id,
        userId,
        email,
        is_client,
        is_technician,
        name
    }
};

const getLuluWright = () => {
    let id = "8d2015d8-51a8-4398-88b0-a570a3d45ede";
    let userId = "46a0d2c4-a924-492a-9e65-179edde76bd3";
    let email = "luluwright@local.com";
    let is_technician = false;
    let is_client = true;
    let name = "Lulu Wright";

    return {
        id,
        userId,
        email,
        is_client,
        is_technician,
        name
    }
};

export default {
    getSammyBear,
    getLuluWright
}