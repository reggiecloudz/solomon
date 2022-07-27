import { Component, OnInit } from '@angular/core';
import { Job } from '../../models/job.model';
import { JobService } from '../../services/job.service';

@Component({
  selector: 'app-list-job',
  templateUrl: './list-job.component.html',
  styleUrls: ['./list-job.component.css']
})
export class ListJobComponent implements OnInit {
  JobList: any = [];

  constructor(
    public jobService: JobService
  ) { }

  ngOnInit(): void {
    this.loadJobs();
  }

  loadJobs() {
    return this.jobService.GetJobs().subscribe((data: {}) => {
      this.JobList = data;
    });
  }

  // Delete job
  deleteJob(data: any){
    var index = this.JobList.map((x: any) => {return x.id}).indexOf(data.id);
     return this.jobService.DeleteJob(data.id).subscribe(res => {
      this.JobList.splice(index, 1)
       console.log('Job deleted!')
     })
  }
}
