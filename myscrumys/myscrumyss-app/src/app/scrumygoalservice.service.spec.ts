import { TestBed, inject } from '@angular/core/testing';

import { ScrumygoalserviceService } from './scrumygoalservice.service';

describe('ScrumygoalserviceService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ScrumygoalserviceService]
    });
  });

  it('should be created', inject([ScrumygoalserviceService], (service: ScrumygoalserviceService) => {
    expect(service).toBeTruthy();
  }));
});
