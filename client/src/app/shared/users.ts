const getSammyBear = () => {
    let id = "650aac83-a1c0-48d1-9841-ed24f388026e";
    let userId = "f1b6bc39-8d8d-429e-b0f6-c02826f7a053";
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
    let id = "54015a07-9e2e-4faf-bf57-8b78297b53af";
    let userId = "4fe8a5f5-f858-4463-91dc-9d752615276f";
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