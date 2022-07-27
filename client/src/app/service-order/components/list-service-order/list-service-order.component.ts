import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ServiceOrder } from '../../models/service-order.model';
import { ServiceOrderService } from '../../services/service-order.service';

@Component({
  selector: 'app-list-service-order',
  templateUrl: './list-service-order.component.html',
  styleUrls: ['./list-service-order.component.css']
})
export class ListServiceOrderComponent implements OnInit {
  deviceId = this.actRoute.snapshot.paramMap.get('id');
  ServiceOrderList: any = [];

  ngOnInit() {
    this.loadServiceOrders();
  }

  constructor(
    private actRoute: ActivatedRoute,
    public serviceOrderService: ServiceOrderService
  ) { }

  loadServiceOrders() {
    return this.serviceOrderService.GetDeviceServiceOrders(Number(this.deviceId)).subscribe((data: {}) => {
      this.ServiceOrderList = data;
    });
  }

  // Delete order
  deleteServiceOrder(data: any){
    var index = this.ServiceOrderList.map((x: any) => {return x.device}).indexOf(data.device);
     return this.serviceOrderService.DeleteServiceOrder(data.id).subscribe(res => {
      this.ServiceOrderList.splice(index, 1)
       console.log('Service Order deleted!')
     })
  }

}
