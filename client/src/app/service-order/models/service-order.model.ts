export class ServiceOrder {
    id!: number;
    problem!: string;
    details!: string;
    is_open!: boolean;
    device!: string;
    offer!: any;
    status!: string;
    followup_dates!: [any];
    technician!: string;
    get_client!: any;
}