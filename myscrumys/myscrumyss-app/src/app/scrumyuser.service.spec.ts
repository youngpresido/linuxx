import { TestBed, inject } from '@angular/core/testing';

import { ScrumyuserService } from './scrumyuser.service';

describe('ScrumyuserService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [ScrumyuserService]
    });
  });

  it('should be created', inject([ScrumyuserService], (service: ScrumyuserService) => {
    expect(service).toBeTruthy();
  }));
});
